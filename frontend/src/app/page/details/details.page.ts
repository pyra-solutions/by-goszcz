import { Component } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { Project } from '../../models/project.model';
import { ActivatedRoute } from '@angular/router';
import { map } from 'rxjs';

interface SejmDocument {
  date: string;
  printNumber: string;
  stageName: string;
  stageType: string;
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

  id = this.randomInt(0, 5);

  constructor(private projectSerivce: ProjectService, private route: ActivatedRoute ) {
    this.pos = this.route.snapshot.paramMap.get('pos')!;

    console.log('faksopdfak', this.id)

    this.projectSerivce.fetchTimeline(this.id).pipe(map((o: any)=>o.stages)).subscribe((r: any)=>{
      console.log('thisfapodsfk', r) 
      this.steps = r;
    })

    this.project = this.projectSerivce.generateProjects(1)[0];
  }

  randomInt(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
}
