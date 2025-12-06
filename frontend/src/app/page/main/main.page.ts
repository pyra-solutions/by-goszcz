import { Component, computed, signal, Signal } from '@angular/core';
import { Router } from '@angular/router';
import { Project, ProjectStatus } from '../../models/project.model';
import { ALL_PROJECT_STATUSES, ProjectService } from '../../services/project.service';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  statusFilters = ALL_PROJECT_STATUSES;
  statusFilter = signal<ProjectStatus | null>(null)

  dateRangeFilter = signal('')
  beginRangeDate = computed(()=>this.dateRangeFilter()[0])
  beginRangeEnd = computed(()=>this.dateRangeFilter()[1])

  selected!: Project;

  titleFilter = signal('')

  projects = signal<Project[]>([]);

  filteredProjects = computed(()=>
    this.projects()
    .filter((p)=>p.title!.includes(this.titleFilter()))
    .filter((p)=>this.statusFilter() == null ? true : p.status == this.statusFilter())
  )

  constructor(private router: Router, private projectService: ProjectService) {
    // this.projects.set(this.projectService.generateProjects(50).map((p)=>({...p, selected: false})))
    this.projectService.fetchProjects().subscribe((p: any)=>{
      this.projects.set(p.slice(0, 100));
    })


    setInterval(()=>{
      console.log('fasdf', this.selected)
    }, 2500)
  }

  goToDetails() {
    this.router.navigate(['details', this.selected.year, this.selected.pos]);
  }

}
