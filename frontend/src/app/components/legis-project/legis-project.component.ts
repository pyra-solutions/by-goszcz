import { Component, Input } from '@angular/core';

@Component({
  selector: 'legis-project',
  templateUrl: './legis-project.component.html',
  styleUrls: ['./legis-project.component.scss'],
  standalone: false,
})
export class LegisProjectComponent {
  @Input({required: true}) selected = false;
  @Input({required: true}) name!: string;
  @Input({required: true}) source!: string;
  @Input({required: true}) status!: string;
  @Input({required: true}) step!: string;

  // constructor() {
  //   setInterval(()=>{
  //     console.log('goajdog', this.selected)
  //   }, 2500)
  // }
}
