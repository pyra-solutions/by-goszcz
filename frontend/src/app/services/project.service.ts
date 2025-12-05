import { Injectable } from '@angular/core';
import { faker } from '@faker-js/faker';
import { Project, ProjectStatus } from '../models/project.model';

@Injectable({
  providedIn: 'root',
})
export class ProjectService {
  private readonly statuses: ProjectStatus[] = ['W TOKU', 'ZAKOŃCZONY', 'OCZEKUJE'];

  generateProjects(count: number = 8): Project[] {
    // faker.setLocale('pl');

    const projects: Project[] = [];

    for (let i = 1; i <= count; i++) {
      projects.push({
        id: i,
        title: `Projekt ustawy o ${faker.word.words(2)}`,
        description: faker.lorem.sentence(),
        status: faker.helpers.arrayElement(this.statuses),
        updatedAt: faker.date.recent({ days: 10 }),
      });
    }

    return projects;
  }
}
