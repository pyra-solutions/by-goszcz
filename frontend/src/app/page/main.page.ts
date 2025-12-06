import { Component } from '@angular/core';

@Component({
  selector: 'main-page',
  templateUrl: './main.page.html',
  styleUrls: ['./main.page.scss'],
  standalone: false,
})
export class MainPage {
  // selected: false, 
  fakeProjects = Array(5).fill({
    name: 'Zmiana ustawy o systemie oswiaty',
    source: 'druk nr 1175 MEN',
    status: 'finished',
    step: 'dzu poz'
  })
}
