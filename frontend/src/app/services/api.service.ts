import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class ApiService {
  private path = 'http://192.168.1.161:8000/api/';
  private headers = new Headers({
    'Content-Type': 'application/json'
  });
  private options = new RequestOptions({ headers: this.headers });

  constructor(private http: Http) {}

  private getParamsString(params: any) {
    return Object.keys(params).map(key => `&${key}=${params[key]}`)
      .join('');
  }

  public get(path: string, params={}) {
    return this.http.get(`${this.path}${path}?format=json${this.getParamsString(params)}`, this.options)
      .map(res => res.json());
  }

  public post(path: string, body: any) {
    return this.http.post(`${this.path}${path}?format=json`,
      JSON.stringify(body),
      this.options)
      .map(res => res.json());
  }
}
