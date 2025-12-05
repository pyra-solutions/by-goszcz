import { Component } from '@angular/core';
import { TranslocoService } from '@jsverse/transloco';

@Component({
  selector: 'language-selector',
  templateUrl: './language-selector.component.html',
  styleUrls: ['./language-selector.component.scss'],
  standalone: false,
})
export class LanguageSelectorComponent {
  languageSelected = 'pl';
  languagesAvailable = ['pl', 'en', 'ua'];

  constructor(private transloco: TranslocoService) {
    this.languageSelected = this.transloco.getActiveLang();
  }

  languageChanged() {
    console.log(this.languageSelected);
    this.transloco.setActiveLang(this.languageSelected.slice(0, 2));
  }
}
