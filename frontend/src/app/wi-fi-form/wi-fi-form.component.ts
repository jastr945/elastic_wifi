import { Component, OnInit } from '@angular/core';
import { WiFi } from '../search/search.model';

@Component({
  selector: 'app-wi-fi-form',
  templateUrl: './wi-fi-form.component.html',
  styleUrls: ['./wi-fi-form.component.css']
})
export class WiFiFormComponent implements OnInit {

  model = new WiFi('110 NW 10th Ave', '2mi');

  submitted = false;

  onSubmit() { this.submitted = true; }

  // TODO: Remove this when we're done
  get diagnostic() { return JSON.stringify(this.model); }

}
