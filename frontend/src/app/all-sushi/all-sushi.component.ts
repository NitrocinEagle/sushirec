import { Component } from '@angular/core';

import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { ApiService } from '../services/api.service';

@Component({
  selector: 'all-sushi',
  templateUrl: './all-sushi.component.html',
  styleUrls: ['./all-sushi.component.css']
})
export class AllSushiComponent {
  private cards$: Observable<any>;

  constructor(private apiService: ApiService) {
    this.cards$ = apiService.get('')
      .map(res => res.data);
  }
}
