import { Component, computed, signal, Signal } from '@angular/core';
import { Router } from '@angular/router';
import { Project, ProjectStatus } from '../../models/project.model';
import { ALL_PROJECT_STATUSES, ProjectService } from '../../services/project.service';
import { DateTime, Interval } from 'luxon';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  generatingSummary = false;
  aiResponse: any;
  aiSummaryFileName: string = '';

  statusFilters = ALL_PROJECT_STATUSES;
  publisherFilters: string[] = ['DU', 'MP'];

  typeFilters = ['Ustawa', 'Rozporządzenie', 'Obwieszczenie']
  typeFilter = signal(null)

  statusFilter = signal<ProjectStatus | null>(null)

  dateAnnouncementRangeFilter = signal('')
  beginAnnouncementRangeDate = computed<Date>(()=>this.dateAnnouncementRangeFilter()?.[0] as any as Date)
  endAnnouncementRangeDate = computed<Date>(()=>this.dateAnnouncementRangeFilter()?.[1] as any as Date)

  dateChangeRangeFilter = signal('')
  beginChangeRangeDate = computed<Date>(()=>this.dateAnnouncementRangeFilter()?.[0] as any as Date)
  endChangeRangeDate = computed<Date>(()=>this.dateAnnouncementRangeFilter()?.[1] as any as Date)

  selected = signal<Project | null>(null);

  titleFilter = signal('')
  publisherFilter = signal(null);

  projects = signal<Project[]>([]);

  filteredProjects = computed(()=>
    this.projects()
    .filter((p)=>p.title!.includes(this.titleFilter()))
    .filter((p)=>this.statusFilter() == null ? true : p.status == this.statusFilter())
    .filter((p)=>this.publisherFilter() == null ? true : p.publisher == this.publisherFilter())
    .filter((p)=> {
      if(this.beginAnnouncementRangeDate() && this.endAnnouncementRangeDate()) {
        const pdate = DateTime.fromJSDate(new Date(p.announcement_date!))
        const edate = DateTime.fromJSDate(this.endAnnouncementRangeDate())
        const sdate = DateTime.fromJSDate(this.beginAnnouncementRangeDate())

        console.log(pdate.toISO(), edate.toISO(), sdate.toISO())
  
        // return (Interval.fromDateTimes(sdate, edate) as any).includes(pdate)
        return Interval.fromDateTimes(sdate, edate).contains(pdate)
      } 
      else if(this.beginAnnouncementRangeDate()) {
        const pdate = DateTime.fromJSDate(new Date(p.announcement_date!))
        const exactDate = DateTime.fromJSDate(new Date(this.beginAnnouncementRangeDate()))

        return pdate.toISODate() == exactDate.toISODate();
      }
      else {
        return true;
      }
    })
    .filter((p)=>this.typeFilter() == null ? true : p.act_type == this.typeFilter())
  )

  constructor(private router: Router, private projectService: ProjectService) {
    for(let i = 1; i < 100; i++) {
      this.projectService.fetchProjects(i).subscribe((p: any)=>{
        this.projects.set([...this.projects(), ...p.slice(0, 20)]);
      })
    }
  }

  refreshSelected() {
    this.aiResponse = null;
  }

  goToDetails() {
    this.router.navigate(['details', this.selected()!.pos, this.selected()!.title]);
  }

  generateAiSummary() {
    this.aiSummaryFileName = this.selected()!.title!
    this.generatingSummary = true;

    this.projectService.fetchSummary(String(this.selected()!.pos!)).subscribe((res: any)=>{
      console.log('Ai response', res)
      console.log('Ai response', JSON.parse(res.response.analysis))
      this.aiResponse = JSON.parse(res.response.analysis)
      this.generatingSummary = false;
    })
  }
}
