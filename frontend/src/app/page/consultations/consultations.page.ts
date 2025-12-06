import { Component, computed, signal } from '@angular/core';
import { Router } from '@angular/router';
import { PROJECT_CONSULTATIONS, ProjectConsultation } from '../../models/project.model';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'consultations-page',
  templateUrl: './consultations.page.html',
  styleUrls: ['./consultations.page.scss'],
  standalone: false,
})
export class ConsultationsPage {

  titleFilter = signal('');

  selected!: ProjectConsultation;

  consultations = signal(PROJECT_CONSULTATIONS);

  consultationsFiltered = computed(()=>
    this.consultations()
    .filter((c)=>c.project_name.includes(this.titleFilter()))
  )

  constructor(private router: Router, private projectService: ProjectService) {
  }
}
