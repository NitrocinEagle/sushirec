import { Component, Input } from '@angular/core';
import { ApiService } from '../services/api.service';
@Component({
  selector: 'sushi-card',
  templateUrl: './sushi-card.component.html',
  styleUrls: ['./sushi-card.component.css']
})
export class SushiCardComponent {
  @Input() card: any;
  private chosen: boolean = false;
  constructor(private apiService: ApiService) {}

  chooseSushi() {
    this.chosen = true;
    let body: any = {
      choice: this.card.sushi_id
    };
    if (localStorage.getItem('userId')) {
      body.user_id = localStorage.getItem('userId');
    }

    this.apiService.post('set-choice/', body)
      .subscribe(response => {
        localStorage.setItem('userId', response.user_id);
      });
  }
}
