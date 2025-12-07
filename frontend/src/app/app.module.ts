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
import { TimelineModule } from 'primeng/timeline';
import { Badge } from 'primeng/badge';
import { LegisProjectComponent } from './components/legis-project/legis-project.component';
import { LegisTopbarComponent } from './components/legis-topbar/legis-topbar.component';
import { MainPage } from './page/main/main.page';
import { ScrollerModule } from 'primeng/scroller';
import { DetailsPage } from './page/details/details.page';
import { CardModule } from 'primeng/card';
import { DatePickerModule } from 'primeng/datepicker';
import { FloatLabelModule } from 'primeng/floatlabel';
import { ConsultationsPage } from './page/consultations/consultations.page';
import { ProgressBarModule } from 'primeng/progressbar';
import { PanelModule } from 'primeng/panel';
import { AccordionModule } from 'primeng/accordion';
import { DialogModule } from 'primeng/dialog';
import { ConsultationCommentsComponent } from './page/comments/comments.page';


@NgModule({
  declarations: [
    AppComponent,
    LanguageSelectorComponent,
    LegisProjectComponent,
    LegisTopbarComponent,
    MainPage,
    DetailsPage,
    ConsultationsPage,
    ConsultationCommentsComponent
  ],
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
    TimelineModule,
    Badge,
    ScrollerModule,
    TimelineModule,
    CardModule,
    DatePickerModule,
    FloatLabelModule,
    InputTextModule,
    ProgressBarModule,
    PanelModule,
    AccordionModule,
    DialogModule,
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
export class AppModule { }
