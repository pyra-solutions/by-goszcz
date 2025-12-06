import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Consultation, Project } from '../../models/project.model';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'consultations-page',
  templateUrl: './consultations.page.html',
  styleUrls: ['./consultations.page.scss'],
  standalone: false,
})
export class ConsultationsPage {
  selected!: Project;
  projects: Project[] = []

  // consultations: Consultation[] ;

  constructor(private router: Router, private projectService: ProjectService) {
    this.projects = this.projectService.generateProjects(50).map((p)=>({...p, selected: false}))
  }

  goToDetails() {
    this.router.navigate(['details', this.selected.year, this.selected.pos]);
  }
}
