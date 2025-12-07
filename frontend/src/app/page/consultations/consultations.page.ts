import { Component, computed, signal } from '@angular/core';
import { Router } from '@angular/router';
import { ProjectConsultation } from '../../models/project.model';
import { ProjectService } from '../../services/project.service';

@Component({
  selector: 'consultations-page',
  templateUrl: './consultations.page.html',
  styleUrls: ['./consultations.page.scss'],
  standalone: false,
})
export class ConsultationsPage {

  titleFilter = signal('');

  statusMappings = {
    'in_progress': 'W trakcie',
    'finished': 'Zakończony',
  }

  // statusFilters = ['Zakończony', 'W trakcie zaplanowany']
  // statusFilter = signal<ConsultationStatus | null>(null)

  selected!: ProjectConsultation;

  consultations = signal<ProjectConsultation[]>([]);

  consultationsFiltered = computed(()=>
    this.consultations()
    .filter((c)=>c.project_name.includes(this.titleFilter()))
    // .filter((p)=>this.statusFilter() == null ? true : p.status == this.statusFilter())
  )

  constructor(private router: Router, private projectService: ProjectService) {
    this.projectService.fetchConsultations(1).subscribe((r: any)=>{
      console.log('consulttations', r)
      this.consultations.set(r)
    })
  }

  getPdfLink(consultationId: string) {
    return `https://orka.sejm.gov.pl/Druki10ka.nsf/dok1?OpenAgent&10-${consultationId.replaceAll('/','-')}`
  }

  mapStatus(status: string) {
    return (this.statusMappings as any)[status];
  }
  
  openComments() {
    if(this.selected.status != 'finished') {
      alert('Nie można podejrzeć komentarzy nie ukończonych konsultacji')
    }
    else {
      this.router.navigate(['comments', this.selected.consultation_id]);
    }
  }
}
