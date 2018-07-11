import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule }   from '@angular/forms';
import { AgmCoreModule } from '@agm/core';

import { AppComponent } from './app.component';
import { WiFiApiService } from './search/search-api.service';
import { WiFiFormComponent } from './wi-fi-form/wi-fi-form.component';
import { GooglePlaceModule } from "ngx-google-places-autocomplete";

@NgModule({
  declarations: [
    AppComponent,
    WiFiFormComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    GooglePlaceModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyDwXSv7Ru8m3iNX6CUDmNVZ_gIBSbJO4GQ'
    }),
  ],
  providers: [WiFiApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
