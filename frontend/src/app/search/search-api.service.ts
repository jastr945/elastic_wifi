import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import 'rxjs/add/operator/map';
import {WiFi} from './search.model';

@Injectable()
export class WiFiApiService {

  // private _WiFiURL = "https://arli63b60f.execute-api.us-west-2.amazonaws.com/api/";
  private _WiFiURL = 'http://127.0.0.1:8001/';
  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of matching locations
  getWiFi(): Observable<WiFi[]> {
    return this.http.get<WiFi[]>(this._WiFiURL)
      .do(res => console.log(res["locations"]))
      .catch(WiFiApiService._handleError);
  }
}
