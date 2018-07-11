import {Component, OnInit} from '@angular/core';
import {NgForm} from '@angular/forms';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {Subscription} from 'rxjs/Subscription';
import {WiFi} from '../search/search.model';
import {Search} from '../query/query.interface';
import {Error} from './error.model';
import {WiFiApiService} from '../search/search-api.service';


@Component({
  selector: 'app-wi-fi-form',
  templateUrl: './wi-fi-form.component.html',
  styleUrls: ['./wi-fi-form.component.css']
})
export class WiFiFormComponent implements OnInit {

  search: Search = {
    address: '',
    distance: 0.2
  };

  WiFiListSubs: Subscription;
  WiFiList: WiFi[];
  Error: Error;

  constructor(private WiFiApi: WiFiApiService, private http: HttpClient) {
  }

  onSubmit({ value, valid }: { value: Search, valid: boolean }) {
    console.log(value, valid);
    this.http.post('http://127.0.0.1:8001/', value)
    .subscribe(response => {
      console.log(response);
      this.WiFiList = response["locations"];
      this.Error = "";
    },(err: HttpErrorResponse) => {
      console.log(err);
      this.Error = err["error"]["Message"];
      this.WiFiList = [];
    });
  }


  ngOnInit() {

  }

}
