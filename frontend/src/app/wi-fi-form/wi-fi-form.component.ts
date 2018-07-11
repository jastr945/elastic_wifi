import {Component, ViewChild} from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { GooglePlaceDirective } from '../../../node_modules/ngx-google-places-autocomplete/ngx-google-places-autocomplete.directive';
import { ComponentRestrictions } from "../../../node_modules/ngx-google-places-autocomplete/objects/options/componentRestrictions";
import {WiFi} from '../search/search.model';
import {Search} from '../query/query.interface';
import {Error} from './error.model';


@Component({
  selector: 'app-wi-fi-form',
  templateUrl: './wi-fi-form.component.html',
  styleUrls: ['./wi-fi-form.component.css']
})
export class WiFiFormComponent {
  @ViewChild('places') places: GooglePlaceDirective;

  public changeConfig() {
    this.places.options.componentRestrictions = new ComponentRestrictions({
      country: "us"
    });

    this.places.reset();
  }

  lat: number = 45.5122;
  lng: number = -122.6587;

  search: Search = {
    address: '',
    distance: 0.2
  };

  WiFiList: WiFi[];
  Error: Error;

  constructor(private http: HttpClient) {
  }

  onChange(search: Search) {
    this.search.address = search["formatted_address"];
  }

  onSubmit() {
    console.log(this.search);
    this.http.post('https://arli63b60f.execute-api.us-west-2.amazonaws.com/api/', this.search)
    .subscribe(response => {
      console.log(response);
      this.WiFiList = response["locations"];
      this.Error = null;
    },(err: HttpErrorResponse) => {
      console.log(err);
      this.Error = err["error"]["Message"];
      this.WiFiList = [];
    });
  }

  onMouseOver(infoWindow, gm) {
    gm.lastOpen = infoWindow;
    infoWindow.open();
  }

  onMouseOut(infoWindow, gm) {
    gm.lastOpen = infoWindow;
    gm.lastOpen.close();
  }

  ngOnInit() {

  }

}
