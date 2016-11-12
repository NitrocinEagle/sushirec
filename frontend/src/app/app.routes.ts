import { Routes } from '@angular/router';

import { AllSushiComponent } from './all-sushi/all-sushi.component';
import { RecommendedSushiComponent } from './recommended-sushi/recommended-sushi.component';

export const ROUTES: Routes = [
  {
    path: '',
    pathMatch: 'full',
    redirectTo: 'all'
  },
  {
    path: 'all',
    component: AllSushiComponent
  },
  {
    path: 'recommended',
    component: RecommendedSushiComponent
  },
]
