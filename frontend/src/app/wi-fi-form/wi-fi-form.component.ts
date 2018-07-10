import { Component, OnInit } from '@angular/core';
import { WiFi } from '../search/search.model';
import {Subscription} from 'rxjs/Subscription';
import {WiFiApiService} from '../search/search-api.service';
import { Search } from './search.interface';

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

  constructor(private WiFiApi: WiFiApiService) {
  }

  onSubmit({ value, valid }: { value: Search, valid: boolean }) {
    console.log(value, valid);
  }


  ngOnInit() {

  }

}
