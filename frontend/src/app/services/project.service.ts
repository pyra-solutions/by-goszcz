import { Injectable } from '@angular/core';
import { Project, ProjectStatus } from '../models/project.model';

@Injectable({
  providedIn: 'root',
})
export class ProjectService {
  // Definicja stałej listy wszystkich dostępnych statusów
  private readonly ALL_PROJECT_STATUSES: ProjectStatus[] = [
    "akt indywidualny",
    "akt jednorazowy",
    "akt objęty tekstem jednolitym",
    "akt posiada tekst jednolity",
    "bez statusu",
    "brak mocy prawnej",
    "nieobowiązujący - przyczyna nieustalona",
    "nieobowiązujący - uchylona podstawa prawna",
    "obowiązujący",
    "tekst jednolity dla aktu jednorazowego",
    "uchylony",
    "uchylony wykazem",
    "uznany za uchylony",
    "wydane z naruszeniem prawa",
    "wygaśnięcie aktu"
  ];

  constructor() { }

  private getRandomInt(min: number, max: number): number {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  private getRandomDate(startYear: number, endYear: number): Date {
    const start = new Date(startYear, 0, 1).getTime();
    const end = new Date(endYear, 11, 31).getTime();
    const randomTime = start + Math.random() * (end - start);
    return new Date(randomTime);
  }

  /**
   * Tworzy pojedynczy, losowy obiekt Project, używając nowych statusów.
   */
  private createRandomProject(index: number): Project {
    const types = ["Uchwała", "Rozporządzenie", "Ustawa", "Dyrektywa"];
    const publishers = ["Ministerstwo Cyfryzacji", "Kancelaria Sejmu", "Prezydent RP", "Rada Ministrów"];

    const randomYear = this.getRandomInt(2020, 2025);
    const randomVolume = this.getRandomInt(1, 100);
    const randomPos = this.getRandomInt(1, 5000);

    const titlePrefix = types[this.getRandomInt(0, types.length - 1)];

    return {
      id: index + 1,
      publisher: publishers[this.getRandomInt(0, publishers.length - 1)],
      year: randomYear,
      volume: randomVolume,
      pos: randomPos,
      title: `${titlePrefix} nr ${index + 1}/${randomVolume}/${randomYear} w sprawie ${Math.random() > 0.5 ? 'nowelizacji' : 'utworzenia'} systemu X`,
      display_address: `Dz.U. poz. ${randomPos} z ${randomYear} r.`,
      promulgation: `Dziennik Urzędowy z dnia ${this.getRandomDate(randomYear, randomYear).toLocaleDateString('pl-PL')}`,
      announcement_date: this.getRandomDate(randomYear - 1, randomYear),
      text_pdf: Math.random() > 0.3,
      text_html: Math.random() > 0.5,
      change_date: Math.random() > 0.7 ? this.getRandomDate(randomYear, 2025) : undefined,
      eli: `http://eli.example.pl/${randomYear}/${randomVolume}/${randomPos}`,
      type: titlePrefix,
      // Losowanie statusu z Twojej listy
      status: this.ALL_PROJECT_STATUSES[this.getRandomInt(0, this.ALL_PROJECT_STATUSES.length - 1)],
    };
  }

  /**
   * Publiczna metoda do generowania tablicy losowych projektów.
   */
  public generateProjects(count: number): Project[] {
    const projects: Project[] = [];
    for (let i = 0; i < count; i++) {
      projects.push(this.createRandomProject(i));
    }
    return projects;
  }
}
