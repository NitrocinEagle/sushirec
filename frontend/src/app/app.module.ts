import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule }   from '@angular/router';

import { MaterialModule } from '@angular/material';

import { AppComponent } from './app.component';

import { ROUTES } from './app.routes';
import { ApiService } from './services/api.service';
import { AllSushiComponent } from './all-sushi/all-sushi.component';
import { RecommendedSushiComponent } from './recommended-sushi/recommended-sushi.component';
import { SushiCardComponent } from './sushi-card/sushi-card.component';

@NgModule({
  declarations: [
    AppComponent,
    AllSushiComponent,
    RecommendedSushiComponent,
    SushiCardComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(ROUTES),
    MaterialModule.forRoot()
  ],
  providers: [
    ApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
