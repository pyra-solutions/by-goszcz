import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: false,
})
export class AppComponent implements OnInit{
  constructor(private router: Router) {}

  ngOnInit(): void {
    setInterval(()=>{
      console.log('gkaposdgka', this.router.url)
    }, 2500)
  }

  getRoute() {
    return this.router.url.split('/')[1];
  }


  isHomeActive() {
    const route = this.getRoute();

    return route == 'home' || route == 'details'
  }

  isConsultationsActive() {
    const route = this.getRoute();

    return route == 'consultations' || route == 'comments'
  }

  goto(route: string) {
    this.router.navigateByUrl(route);
  }
}
