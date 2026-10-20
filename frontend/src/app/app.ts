import { Component, inject } from '@angular/core';
import { toSignal } from '@angular/core/rxjs-interop';
import { HealthService } from './core/api/health.service';

@Component({
  selector: 'app-root',
  template: `
    <h1>CloudVanguard</h1>
    <p>API says: {{ health()?.status ?? 'connecting...' }}</p>
  `,
})
export class App {
  private healthService = inject(HealthService);
  health = toSignal(this.healthService.getHealth());
}