import { Component } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { Project } from '../../models/project.model';

interface LegislativeStep {
  title: string;
  shortTitle: string;
  description: string;
  chamber: 'Sejm' | 'Senat' | 'Prezydent' | 'Inne';
  date?: string;
  status: 'zakończony' | 'w toku' | 'planowany';
}

@Component({
  selector: 'details-page',
  templateUrl: './details.page.html',
  styleUrls: ['./details.page.scss'],
  standalone: false
})
export class DetailsPage {

  project!: Project;

  constructor(private projectSerivce: ProjectService) {
    // this.project = this.projectSerivce.generateProjects(1)[0];
  }

  steps: LegislativeStep[] = [
    {
      title: 'Inicjatywa ustawodawcza i wniesienie projektu ustawy',
      shortTitle: 'Inicjatywa',
      description:
        'Projekt ustawy jest przygotowywany i wnoszony do Sejmu przez uprawniony podmiot (np. posłów, Senat, Prezydenta, Radę Ministrów lub obywateli).',
      chamber: 'Inne',
      date: 'Etap 1',
      status: 'zakończony'
    },
    {
      title: 'I czytanie projektu ustawy w Sejmie',
      shortTitle: 'I czytanie',
      description:
        'Projekt trafia do komisji sejmowych lub jest rozpatrywany na posiedzeniu plenarnym. Przedstawiane są główne założenia i uzasadnienie projektu.',
      chamber: 'Sejm',
      date: 'Etap 2',
      status: 'zakończony'
    },
    {
      title: 'II czytanie projektu ustawy w Sejmie',
      shortTitle: 'II czytanie',
      description:
        'Przedstawiane jest sprawozdanie komisji. Posłowie mogą zgłaszać poprawki i dodatkowe wnioski.',
      chamber: 'Sejm',
      date: 'Etap 3',
      status: 'zakończony'
    },
    {
      title: 'III czytanie i uchwalenie ustawy przez Sejm',
      shortTitle: 'III czytanie',
      description:
        'Odbywa się debata nad zgłoszonymi poprawkami oraz głosowanie nad całością ustawy. Po uchwaleniu ustawa jest przekazywana do Senatu.',
      chamber: 'Sejm',
      date: 'Etap 4',
      status: 'zakończony'
    },
    {
      title: 'Prace nad ustawą w Senacie',
      shortTitle: 'Senat',
      description:
        'Senat może przyjąć ustawę bez zmian, wprowadzić poprawki lub odrzucić ją w całości. Następnie ustawa wraca do Sejmu, który może odrzucić stanowisko Senatu bezwzględną większością głosów.',
      chamber: 'Senat',
      date: 'Etap 5',
      status: 'w toku'
    },
    {
      title: 'Podpis ustawy przez Prezydenta RP',
      shortTitle: 'Prezydent',
      description:
        'Prezydent może ustawę podpisać, odmówić podpisania (weto) lub skierować ją do Trybunału Konstytucyjnego w celu zbadania zgodności z Konstytucją.',
      chamber: 'Prezydent',
      date: 'Etap 6',
      status: 'planowany'
    },
    {
      title: 'Ogłoszenie ustawy w Dzienniku Ustaw i wejście w życie',
      shortTitle: 'Ogłoszenie',
      description:
        'Po podpisaniu ustawy następuje jej ogłoszenie w Dzienniku Ustaw. Zwykle po upływie vacatio legis ustawa wchodzi w życie.',
      chamber: 'Inne',
      date: 'Etap 7',
      status: 'planowany'
    }
  ];

}
