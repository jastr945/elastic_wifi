import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/do';
import {WiFi} from './search.model';

@Injectable()
export class WiFiApiService {

  private _WiFiURL = "https://arli63b60f.execute-api.us-west-2.amazonaws.com/api/";

  constructor(private http: HttpClient) {
  }

  private static _handleError(err: HttpErrorResponse | any) {
    return Observable.throw(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getWiFi(): Observable<WiFi[]> {
    return this.http.get<WiFi[]>(this._WiFiURL)
      .do(data => console.log('All: ' + JSON.stringify(data)))
      .catch(WiFiApiService._handleError);
  }
}
