import { Component } from '@angular/core';
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
  projects: Project[] = []

  constructor(private router: Router, private projectService: ProjectService) {
    this.projects = this.projectService.generateProjects(50).map((p)=>({...p, selected: false}))
  }

  selectProject(index: number) {
    console.log('gjasoigd', index)

    // this.projects = this.projects.map((p)=>({
    //   ...p,
    //   selected: false
    // }))

    // this.projects[index].selected = true;
    // this.selected = this.projects[index];
  }

  goToDetails() {
    this.router.navigateByUrl('details');
  }

}
