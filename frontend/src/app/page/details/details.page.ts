import { Component } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { Project } from '../../models/project.model';
import { ActivatedRoute } from '@angular/router';

interface SejmDocument {
  address: string | null;
  change_date: string;
  closure_date: string;
  comments: string | null;
  description: string | null;
  display_address: string | null;
  document_date: string;
  document_type: string;
  document_type_enum: string | null;
  e_li: string | null;
  eli: string | null;
  id: number;
  links: string | null;
  number: string;
  passed: boolean;
  process_start_date: string;
  shorten_procedure: boolean;
  term: number;
  title: string;
  title_final: string;
  u_e: string | null;
  ue: string | null;
  urgency_status: string;
  urgency_withdraw_date: string | null;
  web_generated_date: string;
}

@Component({
  selector: 'details-page',
  templateUrl: './details.page.html',
  styleUrls: ['./details.page.scss'],
  standalone: false
})
export class DetailsPage {
  
  pos: string;
  project: Project;
  steps: SejmDocument[] = []

  constructor(private projectSerivce: ProjectService, private route: ActivatedRoute ) {
    this.pos = this.route.snapshot.paramMap.get('pos')!;

    this.projectSerivce.fetchTimeline().subscribe((r: any)=>{
      console.log('thisfapodsfk', r) 
      this.steps = r;
    })

    this.project = this.projectSerivce.generateProjects(1)[0];
  }

}
