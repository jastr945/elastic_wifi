import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {WiFiApiService} from './search/search-api.service';
import {WiFi} from './search/search.model';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/do';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  WiFiListSubs: Subscription;
  WiFiList: WiFi[];

  constructor(private WiFiApi: WiFiApiService) {
  }

  ngOnInit() {
    this.WiFiListSubs = this.WiFiApi
      .getWiFi()
      .subscribe(res => {
          this.WiFiList = res["locations"];
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.WiFiListSubs.unsubscribe();
  }
}
