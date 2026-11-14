export interface Resource {
  id: number;
  resource_id: string;
  name: string;
  resource_type: string;
  region: string;
  monthly_cost_usd: number;
  cpu_utilization: number;
  idle_days: number;
  status: string;
}