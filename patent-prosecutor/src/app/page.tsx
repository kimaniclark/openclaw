// This is your main dashboard page
// In Cursor, you'd highlight this and say "Add a docket table showing patent matters"

export default function Dashboard() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-3xl font-bold mb-8">Patent Prosecutor</h1>
      
      {/* Cursor prompt: "Add stats cards showing total matters, pending OAs, upcoming deadlines" */}
      <div className="grid grid-cols-3 gap-4 mb-8">
        <StatsCard title="Active Matters" value="12" />
        <StatsCard title="Pending Office Actions" value="3" />
        <StatsCard title="Due This Week" value="2" />
      </div>

      {/* Cursor prompt: "Add a table of patent matters with columns for docket#, client, app#, status, deadline" */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Patent Docket</h2>
        {/* Table will go here */}
      </div>
    </main>
  )
}

function StatsCard({ title, value }: { title: string; value: string }) {
  return (
    <div className="bg-white rounded-lg shadow p-6">
      <p className="text-gray-500 text-sm">{title}</p>
      <p className="text-3xl font-bold">{value}</p>
    </div>
  )
}
