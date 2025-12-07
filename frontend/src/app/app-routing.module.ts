import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { MainPage } from './page/main/main.page';
import { DetailsPage } from './page/details/details.page';
import { ConsultationsPage } from './page/consultations/consultations.page';
import { ConsultationCommentsComponent } from './page/comments/comments.page';

const routes: Routes = [
  {path: 'home', component: MainPage},
  {path: 'consultations', component: ConsultationsPage},
  {path: 'details/:pos', component: DetailsPage},
  {path: 'comments/:conId', component: ConsultationCommentsComponent},
  {path: '', redirectTo: 'home', pathMatch: 'full'}, 
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })],
  exports: [RouterModule],
})
export class AppRoutingModule {}
