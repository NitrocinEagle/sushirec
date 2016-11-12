import { Component } from '@angular/core';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { ApiService } from '../services/api.service';

@Component({
  selector: 'recommended-sushi',
  templateUrl: './recommended-sushi.component.html',
  styleUrls: ['./recommended-sushi.component.css']
})
export class RecommendedSushiComponent {
  private cards$: Observable<any>;

  constructor(private apiService: ApiService) {
    const userId = localStorage.getItem('userId')
    if (!userId) {
      this.cards$ = Observable.of([]);
    } else {
      this.cards$ = apiService.get(`recommend/`, {'user_id': userId})
        .map(res => res.data);
    }
  }
}
