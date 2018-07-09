import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule }   from '@angular/forms';

import { AppComponent } from './app.component';
import { WiFiApiService } from './search/search-api.service';
import { WiFiFormComponent } from './wi-fi-form/wi-fi-form.component';

@NgModule({
  declarations: [
    AppComponent,
    WiFiFormComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [WiFiApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
