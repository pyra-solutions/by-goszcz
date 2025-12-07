
import { Component, Input, OnInit } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { ActivatedRoute } from '@angular/router';

export interface ConsultationComment {
  // nr_pyt: number;
  question: string;
  comment_text: string;
  author: string;
}

@Component({
  selector: 'app-consultation-comments',
  templateUrl: './comments.page.html',
  styleUrls: ['./comments.page.scss'],
  standalone: false,
})
export class ConsultationCommentsComponent implements OnInit {
  consultationId!: string;

  @Input() comments: ConsultationComment[] = [];

  constructor(private projectService: ProjectService, private route: ActivatedRoute) {
    this.consultationId = this.route.snapshot.paramMap.get('conId')!;
  }

  ngOnInit(): void {
    this.projectService.fetchComments(this.consultationId.replaceAll('/', '-')).subscribe((r: any)=>{
      console.log('fkasodpfka', r);
      this.comments = r;
    })
  }

}