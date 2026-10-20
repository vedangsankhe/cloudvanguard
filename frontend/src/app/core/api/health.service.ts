import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

export interface HealthResponse {
  status: string;
  service: string;
}

@Injectable({ providedIn: 'root' })
export class HealthService {
  private http = inject(HttpClient);

  getHealth() {
    return this.http.get<HealthResponse>(`${environment.apiUrl}/api/v1/health`);
  }
}