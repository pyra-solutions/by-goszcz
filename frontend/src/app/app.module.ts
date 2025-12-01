import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { providePrimeNG } from 'primeng/config';
import { TableModule } from 'primeng/table';
import { TagModule } from 'primeng/tag';
import { SelectModule } from 'primeng/select';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { MenuModule } from 'primeng/menu';
import { ToolbarModule } from 'primeng/toolbar';
import { SplitButtonModule } from 'primeng/splitbutton';
import { IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';
import { MenubarModule } from 'primeng/menubar';

import Lara from '@primeuix/themes/lara';
import { ButtonModule } from 'primeng/button';
import { HttpClientModule } from '@angular/common/http';
import { TranslocoRootModule } from './transloco-root.module';
import { LanguageSelectorComponent } from './components/language-selector/language-selector.component';

@NgModule({
  declarations: [AppComponent, LanguageSelectorComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    TableModule,
    TagModule,
    SelectModule,
    FormsModule,
    InputTextModule,
    MenuModule,
    ToolbarModule,
    ButtonModule,
    SplitButtonModule,
    IconFieldModule,
    InputIconModule,
    MenubarModule,
    HttpClientModule,
    TranslocoRootModule,
  ],
  providers: [
    provideAnimationsAsync(),
    providePrimeNG({
      theme: {
        preset: Lara,
        options: {
          darkModeSelector: false,
        },
      },
    }),
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
