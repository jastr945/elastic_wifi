import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WiFiFormComponent } from './wi-fi-form.component';

describe('WiFiFormComponent', () => {
  let component: WiFiFormComponent;
  let fixture: ComponentFixture<WiFiFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WiFiFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WiFiFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
