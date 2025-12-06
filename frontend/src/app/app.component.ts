import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  standalone: false,
})
export class AppComponent {
  // selected: false, 
  fakeProjects = Array(5).fill({
    name: 'Zmiana ustawy o systemie oswiaty',
    source: 'druk nr 1175 MEN',
    status: 'finished',
    step: 'dzu poz'
  })
}
