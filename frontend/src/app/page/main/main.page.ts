import { Component, computed, signal, Signal } from '@angular/core';
import { Router } from '@angular/router';
import { Project, ProjectStatus } from '../../models/project.model';
import { ALL_PROJECT_STATUSES, ProjectService } from '../../services/project.service';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  fetched = false;

  statusFilters = ALL_PROJECT_STATUSES;
  publisherFilters: string[] = ['DU', 'MU']

  statusFilter = signal<ProjectStatus | null>(null)

  dateRangeFilter = signal('')
  beginRangeDate = computed(()=>this.dateRangeFilter()[0])
  beginRangeEnd = computed(()=>this.dateRangeFilter()[1])


  selected!: Project;

  titleFilter = signal('')
  publisherFilter = signal(null);

  projects = signal<Project[]>([]);

  filteredProjects = computed(()=>
    this.projects()
    .filter((p)=>p.title!.includes(this.titleFilter()))
    .filter((p)=>this.statusFilter() == null ? true : p.status == this.statusFilter())
    .filter((p)=>this.publisherFilter() == null ? true : p.publisher == this.publisherFilter())
  )

  constructor(private router: Router, private projectService: ProjectService) {
    for(let i = 1; i < 25; i++) {
      this.projectService.fetchProjects(i).subscribe((p: any)=>{
        this.projects.set([...this.projects(), ...p.slice(0, 20)]);
      })
    }


    setInterval(()=>{
      console.log('fasdf', this.selected, this.publisherFilter())
    }, 2500)
  }

  goToDetails() {
    this.router.navigate(['details', this.selected.pos]);
  }

}
