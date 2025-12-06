import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  constructor(private router: Router) {}

  loadProject() {
    this.router.navigateByUrl('details');
  }

  fakeProjects = Array(50).fill({
    name: 'Zmiana ustawy o systemie oswiaty',
    source: 'druk nr 1175 MEN',
    status: 'finished',
    step: 'dzu poz'
  })
}
