import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProjectService } from './services/project.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: false,
})
export class AppComponent implements OnInit{
  constructor(private router: Router, private projects: ProjectService) {
    this.projects.fetchProjects().subscribe((r)=>{
      console.log('res', r)
    })
  }

  ngOnInit(): void {
    setInterval(()=>{
      console.log('gkaposdgka', this.router.url)
    }, 2500)
  }

  getRoute() {
    return this.router.url;
  }


  goto(route: string) {
    this.router.navigateByUrl(route);
  }
}
