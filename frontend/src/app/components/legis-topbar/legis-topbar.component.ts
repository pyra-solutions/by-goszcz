import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'legis-topbar',
  templateUrl: './legis-topbar.component.html',
  styleUrls: ['./legis-topbar.component.scss'],
  standalone: false,
})
export class LegisTopbarComponent implements OnInit {
  fontSize: 'small' | 'medium' | 'large' = 'medium';
  contrastMode: 'normal' | 'black' | 'yellow' | 'white' = 'normal';

  ngOnInit() {
    const savedFontSize = localStorage.getItem('fontSize') as 'small' | 'medium' | 'large';
    if (savedFontSize) {
      this.fontSize = savedFontSize;
      this.applyFontSize();
    }

    const savedContrast = localStorage.getItem('contrastMode') as 'normal' | 'black' | 'yellow' | 'white';
    if (savedContrast) {
      this.contrastMode = savedContrast;
      this.applyContrast();
    }
  }

  setFontSize(size: 'small' | 'medium' | 'large') {
    this.fontSize = size;
    this.applyFontSize();
    localStorage.setItem('fontSize', size);
  }

  applyFontSize() {
    document.body.classList.remove('font-small', 'font-medium', 'font-large');
    document.body.classList.add(`font-${this.fontSize}`);
  }

  setContrast(mode: 'normal' | 'black' | 'yellow' | 'white') {
    this.contrastMode = mode;
    this.applyContrast();
    localStorage.setItem('contrastMode', mode);
  }

  applyContrast() {
    document.body.classList.remove('contrast-normal', 'contrast-black', 'contrast-yellow', 'contrast-white');
    document.body.classList.add(`contrast-${this.contrastMode}`);
  }
}
