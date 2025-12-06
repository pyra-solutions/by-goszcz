import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  selected: any = false;

  constructor(private router: Router) {}

  selectProject(index: number) {
    console.log('gjasoigd', index)

    this.fakeProjects = this.fakeProjects.map((p)=>({
      ...p,
      selected: false
    }))

    this.fakeProjects[index].selected = true;
    this.selected = this.fakeProjects[index];
  }

  goToDetails() {
    this.router.navigateByUrl('details');
  }

  fakeProjects = Array(10).fill({
    name: 'Zmiana ustawy o systemie oswiaty',
    source: 'druk nr 1175 MEN',
    status: 'finished',
    step: 'dzu poz',
    selected: false
  })
}
