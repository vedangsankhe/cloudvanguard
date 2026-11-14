import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import { Resource } from '../models/resource.model';

@Injectable({ providedIn: 'root' })
export class ResourceService {
  private http = inject(HttpClient);

  getResources() {
    return this.http.get<Resource[]>(`${environment.apiUrl}/api/v1/resources`);
  }
}