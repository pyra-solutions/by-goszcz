import { Component, computed, signal, Signal } from '@angular/core';
import { Router } from '@angular/router';
import { Project } from '../../models/project.model';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  selected!: Project;

  titleFilter = signal('')

  projects = signal<Project[]>([]);

  filteredProjects = computed(()=>
    this.projects().filter((p)=>p.title!.includes(this.titleFilter()))
  )

  constructor(private router: Router, private projectService: ProjectService) {
    this.projects.set(this.projectService.generateProjects(50).map((p)=>({...p, selected: false})))

    setInterval(()=>{
      console.log(this.titleFilter())
    }, 2500)
  }

  goToDetails() {
    this.router.navigate(['details', this.selected.year, this.selected.pos]);
  }

}
