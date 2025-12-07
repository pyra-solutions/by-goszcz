import { Component } from '@angular/core';
import { ProjectService } from '../../services/project.service';
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
  title: string;

  mock = {
    "beg": [
      "Opracowanie projektu ustawy przez wnioskodawcę",
      "Przeprowadzenie konsultacji publicznych i uzgodnień międzyresortowych",
      "Przyjęcie projektu przez Radę Ministrów (dla projektów rządowych)",
      "Zgłoszenie projektu do laski marszałkowskiej",
      "Nadanie numeru druku i rejestracja projektu",
      "Ocena formalna projektu przez Kancelarię Sejmu"
    ],

    "mid1": [
      "Projekt wpłynął do Sejmu",
      "Przekazanie projektu do Marszałka Sejmu",
      "Decyzja Marszałka o dalszym trybie procedowania",
      "Analiza projektu przez Prezydium Sejmu",
      "Rozpatrzenie projektu przez Konwent Seniorów",
      "Ustalenie terminu I czytania",
      "Publikacja druku projektu"
    ],

    "mid2": [
      "Skierowano do I czytania na posiedzeniu Sejmu",
      "Wprowadzenie projektu do porządku obrad",
      "Przedstawienie projektu przez wnioskodawcę",
      "Zadawanie pytań posłów",
      "Dyskusja ogólna podczas I czytania"
    ],

    "end": [
      "Rozpatrywanie na forum Sejmu",
      "Zakończenie I czytania",
      "Skierowanie projektu do komisji",
      "Prace komisji: wysłuchanie ekspertów, poprawki, głosowania",
      "Przygotowanie sprawozdania komisji",
      "Przedłożenie sprawozdania Sejmowi",
      "II czytanie projektu ustawy",
      "Debata i zgłaszanie dalszych poprawek",
      "III czytanie i głosowanie nad ustawą"
    ]
  }

  steps: {text: string, date: Date}[] = []


  id = this.randomInt(0, 5);

  constructor(private projectSerivce: ProjectService, private route: ActivatedRoute ) {
    this.pos = this.route.snapshot.paramMap.get('pos')!;
    this.title = this.route.snapshot.paramMap.get('title')!;

    console.log('faksopdfak', this.id)

    // this.projectSerivce.fetchTimeline(this.id).pipe(map((o: any)=>o.stages)).subscribe((r: any)=>{
    // console.log('thisfapodsfk', r) 
    this.steps = [
      { text: this.mock.beg[this.randomInt(0,this.mock.beg.length-1)], date: this.randomDate(new Date(2025, 0, 1), new Date(2025, 2, 1)) }, 
      { text: this.mock.beg[this.randomInt(0,this.mock.beg.length-1)], date: this.randomDate(new Date(2025, 2, 1), new Date(2025, 4, 1)) },
      
      { text: this.mock.mid1[this.randomInt(0, this.mock.mid1.length-1)], date: this.randomDate(new Date(2025, 4, 1), new Date(2025, 6, 1)) },
      { text: this.mock.mid1[this.randomInt(0, this.mock.mid1.length-1)], date: this.randomDate(new Date(2025, 6, 1), new Date(2025, 8, 1)) },

      { text: this.mock.mid2[this.randomInt(0, this.mock.mid2.length-1)], date: this.randomDate(new Date(2025, 8, 1), new Date(2025, 9, 1)) },
      { text: this.mock.mid2[this.randomInt(0, this.mock.mid2.length-1)], date: this.randomDate(new Date(2025, 9, 1), new Date(2025, 10, 1)) },

      { text: this.mock.end[this.randomInt(0, this.mock.end.length-1)], date: this.randomDate(new Date(2025, 10, 1), new Date(2025, 11, 1)) },
      { text: this.mock.end[this.randomInt(0, this.mock.end.length-1)], date: this.randomDate(new Date(2025, 11, 1), new Date(2025, 11, 31)) },
    ]
    // })

    // this.project = this.projectSerivce.generateProjects(1)[0];
  }

  randomInt(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  randomDate(start: Date, end: Date): Date {
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
  }
}
