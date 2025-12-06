import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { MainPage } from './page/main/main.page';
import { DetailsPage } from './page/details/details.page';

const routes: Routes = [
  {path: 'home', component: MainPage},
  {path: 'details', component: DetailsPage},
  // {path: '/', redirectTo: 'home'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })],
  exports: [RouterModule],
})
export class AppRoutingModule {}
