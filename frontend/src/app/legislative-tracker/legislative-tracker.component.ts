import { Component, OnInit } from '@angular/core';
import { Project } from '../models/project.model';
import { ProjectService } from '../services/project.service';

interface WorkflowEvent {
  status: string;
  date: string;
  icon: string;
  color: string;
}

@Component({
  selector: 'app-legislative-tracker',
  templateUrl: './legislative-tracker.component.html',
  styleUrls: ['./legislative-tracker.component.scss'],
  standalone: false,
})
export class LegislativeTrackerComponent implements OnInit {
  projects: Project[] = [];
  selectedProject?: Project;

  workflowEvents: WorkflowEvent[] = [];

  constructor(private projectService: ProjectService) {}

  ngOnInit(): void {
    this.projects = this.projectService.generateProjects(50);
    this.selectedProject = this.projects[0];

    // statyczny timeline – możesz potem powiązać daty z projektem
    this.workflowEvents = [
      {
        status: 'Rząd – przygotowanie projektu',
        date: 'Etap 1',
        icon: 'pi pi-briefcase',
        color: '#22c55e',
      },
      {
        status: 'Sejm – pierwsze czytanie',
        date: 'Etap 2',
        icon: 'pi pi-comments',
        color: '#f97316',
      },
      {
        status: 'Sejm – prace w komisjach',
        date: 'Etap 3',
        icon: 'pi pi-users',
        color: '#f97316',
      },
      {
        status: 'Senat – poprawki',
        date: 'Etap 4',
        icon: 'pi pi-pencil',
        color: '#0ea5e9',
      },
      {
        status: 'Prezydent / Dziennik Ustaw',
        date: 'Etap 5',
        icon: 'pi pi-check',
        color: '#6b7280',
      },
    ];
  }

  onRowSelect(event: { data: Project }) {
    this.selectedProject = event.data;
  }

  getSeverity(status: string): 'success' | 'info' | 'warn' | 'danger' {
    switch (status) {
      case 'W TOKU':
        return 'info';
      case 'ZAKOŃCZONY':
        return 'success';
      case 'OCZEKUJE':
      default:
        return 'warn';
    }
  }
}
