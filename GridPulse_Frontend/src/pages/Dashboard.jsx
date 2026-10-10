
import { useState } from 'react'
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from 'recharts'
import Brand from '../components/Brand'

const productionData = [
  { time: '6 AM', energy: 0.4 },
  { time: '8 AM', energy: 2.1 },
  { time: '10 AM', energy: 4.8 },
  { time: '12 PM', energy: 7.2 },
  { time: '2 PM', energy: 6.4 },
  { time: '4 PM', energy: 3.8 },
  { time: '6 PM', energy: 1.2 },
]

const weeklyData = [
  { day: 'Mon', energy: 18 },
  { day: 'Tue', energy: 22 },
  { day: 'Wed', energy: 19 },
  { day: 'Thu', energy: 26 },
  { day: 'Fri', energy: 24 },
  { day: 'Sat', energy: 29 },
  { day: 'Sun', energy: 25 },
]

const navItems = [
  { name: 'Overview', icon: '◫' },
  { name: 'Energy Analytics', icon: '⌁' },
  { name: 'Weather & Forecast', icon: '☀' },
  { name: 'Alerts', icon: '♧' },
  { name: 'Settings', icon: '⚙' },
]

function Dashboard() {
  const [activePage, setActivePage] = useState('Overview')
  const [notifications, setNotifications] = useState(true)
  const [systemName, setSystemName] = useState('My Solar Installation')
  const [capacity, setCapacity] = useState('5.0')

  function SectionTitle({ title, description }) {
    return (
      <div className="mb-7">
        <p className="text-xs font-semibold tracking-[0.15em] text-[#39845A]">
          GRIDPULSE WORKSPACE
        </p>
        <h2 className="mt-2 text-2xl font-bold text-[#183D30] sm:text-3xl">
          {title}
        </h2>
        <p className="mt-2 text-sm text-[#748078]">{description}</p>
        <p className="mt-2 text-xs text-[#98A39A]">
          Demonstration data — not connected to a live solar system.
        </p>
      </div>
    )
  }

  function Overview() {
    return (
      <>
        <section className="relative mt-8 overflow-hidden rounded-[1.75rem] bg-[#123D32] p-6 text-white sm:p-8">
          <div className="pointer-events-none absolute -right-12 -top-24 h-64 w-64 rounded-full border border-white/10" />
          <div className="relative z-10 flex flex-col justify-between gap-6 sm:flex-row sm:items-center">
            <div>
              <p className="text-xs font-medium tracking-[0.15em] text-[#C8F169]">
                YOUR SOLAR AT A GLANCE
              </p>
              <h2 className="mt-3 text-2xl font-semibold sm:text-3xl">
                Make every ray count.
              </h2>
              <p className="mt-3 max-w-lg text-sm leading-6 text-[#D0DED5]">
                Understand your energy production and discover how your
                solar system contributes to a cleaner future.
              </p>
            </div>
            <div className="flex h-20 w-20 shrink-0 items-center justify-center rounded-3xl bg-white/10 text-5xl">
              ☀
            </div>
          </div>
        </section>

        <section className="mt-8">
          <div className="mb-4 flex items-center justify-between">
            <h2 className="text-lg font-bold text-[#183D30]">
              Performance Summary
            </h2>
            <span className="text-xs text-[#879188]">Sample data</span>
          </div>
          <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
            {[
              { label: "Today's Production", value: '24.8', unit: 'kWh', icon: '☀', note: 'Sample daily generation' },
              { label: 'Total Energy', value: '1,284', unit: 'kWh', icon: '↗', note: 'Illustrative lifetime total' },
              { label: 'System Capacity', value: capacity, unit: 'kW', icon: '⚡', note: 'Example installation size' },
              { label: 'System Efficiency', value: '92', unit: '%', icon: '◉', note: 'Illustrative efficiency' },
            ].map((item) => (
              <div key={item.label} className="rounded-2xl border border-[#E3EAE0] bg-white p-5 shadow-sm">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-sm text-[#748078]">{item.label}</span>
                  <span className="flex h-10 w-10 items-center justify-center rounded-xl bg-[#EFF6EA] text-xl">{item.icon}</span>
                </div>
                <p className="mt-5 text-3xl font-bold text-[#183D30]">
                  {item.value} <span className="text-base font-medium">{item.unit}</span>
                </p>
                <p className="mt-2 text-xs text-[#39845A]">{item.note}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="mt-8 rounded-2xl border border-[#E3EAE0] bg-white p-5 sm:p-7">
          <h2 className="text-lg font-bold text-[#183D30]">Solar Production</h2>
          <p className="mt-2 text-sm text-[#748078]">Example generation throughout the day.</p>
          <div className="mt-6 h-72">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={productionData}>
                <defs>
                  <linearGradient id="energyFill" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stopColor="#39845A" stopOpacity={0.3} />
                    <stop offset="95%" stopColor="#39845A" stopOpacity={0.02} />
                  </linearGradient>
                </defs>
                <CartesianGrid stroke="#E8EEE6" strokeDasharray="4 4" vertical={false} />
                <XAxis dataKey="time" tick={{ fill: '#879188', fontSize: 12 }} />
                <YAxis tick={{ fill: '#879188', fontSize: 12 }} />
                <Tooltip formatter={(value) => [`${value} kWh`, 'Energy']} />
                <Area type="monotone" dataKey="energy" stroke="#247A58" strokeWidth={3} fill="url(#energyFill)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </section>
      </>
    )
  }

  function EnergyAnalytics() {
    return (
      <>
        <SectionTitle title="Energy Analytics" description="Explore sample solar generation patterns." />
        <div className="grid gap-4 sm:grid-cols-3">
          {[
            ['Weekly Generation', '163 kWh'],
            ['Daily Average', '23.3 kWh'],
            ['Best Day', '29 kWh'],
          ].map(([label, value]) => (
            <div key={label} className="rounded-2xl border border-[#E3EAE0] bg-white p-6">
              <p className="text-sm text-[#748078]">{label}</p>
              <p className="mt-4 text-3xl font-bold text-[#174B38]">{value}</p>
            </div>
          ))}
        </div>
        <section className="mt-6 rounded-2xl border border-[#E3EAE0] bg-white p-5 sm:p-7">
          <h3 className="text-lg font-bold text-[#183D30]">Weekly Energy Production</h3>
          <div className="mt-6 h-80">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={weeklyData}>
                <CartesianGrid stroke="#E8EEE6" strokeDasharray="4 4" vertical={false} />
                <XAxis dataKey="day" tick={{ fill: '#879188', fontSize: 12 }} />
                <YAxis tick={{ fill: '#879188', fontSize: 12 }} />
                <Tooltip formatter={(value) => [`${value} kWh`, 'Generation']} />
                <Bar dataKey="energy" fill="#39845A" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </section>
      </>
    )
  }

  function WeatherForecast() {
    return (
      <>
        <SectionTitle title="Weather & Forecast" description="Sample conditions that can affect solar generation." />
        <div className="grid gap-5 md:grid-cols-2">
          <div className="rounded-2xl bg-[#123D32] p-7 text-white">
            <p className="text-sm text-[#D0DED5]">Illustrative current conditions</p>
            <div className="mt-5 flex items-center justify-between">
              <div>
                <p className="text-5xl font-semibold">29°C</p>
                <p className="mt-3 text-sm text-[#D0DED5]">Partly cloudy · Demo</p>
              </div>
              <span className="text-6xl">⛅</span>
            </div>
            <p className="mt-6 text-sm text-[#D0DED5]">Location and live weather have not been configured.</p>
          </div>
          <div className="rounded-2xl border border-[#E3EAE0] bg-white p-7">
            <h3 className="text-lg font-bold text-[#183D30]">Solar Outlook</h3>
            <p className="mt-3 text-sm leading-6 text-[#748078]">
              Clearer skies generally provide more sunlight for solar panels.
              Cloud cover can reduce generation. This is general guidance,
              not a live forecast.
            </p>
          </div>
        </div>
        <div className="mt-6 rounded-2xl border border-[#E3EAE0] bg-white p-6">
          <h3 className="font-bold text-[#183D30]">Forecast Preview</h3>
          <div className="mt-5 grid grid-cols-2 gap-3 sm:grid-cols-4">
            {[
              ['Today', '⛅', 'Partly cloudy'],
              ['Tomorrow', '☀', 'Mostly sunny'],
              ['Day 3', '🌦️', 'Possible showers'],
              ['Day 4', '☀', 'Mostly sunny'],
            ].map(([day, icon, description]) => (
              <div key={day} className="rounded-xl bg-[#F6F8F5] p-4 text-center">
                <p className="text-sm font-semibold">{day}</p>
                <p className="my-3 text-3xl">{icon}</p>
                <p className="text-xs text-[#748078]">{description}</p>
              </div>
            ))}
          </div>
        </div>
      </>
    )
  }

  function Alerts() {
    return (
      <>
        <SectionTitle title="System Alerts" description="Review notifications for your solar installation." />
        <div className="rounded-2xl border border-[#DDE9D9] bg-white p-6">
          <div className="flex items-start gap-4">
            <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-[#EFF6EA] text-xl">✓</span>
            <div>
              <h3 className="font-semibold text-[#174B38]">No active demo alerts</h3>
              <p className="mt-2 text-sm leading-6 text-[#748078]">
                This is sample content. Actual fault warnings and production
                alerts require data from your solar equipment or monitoring service.
              </p>
            </div>
          </div>
        </div>
        <div className="mt-5 rounded-2xl border border-[#E3EAE0] bg-white p-6">
          <h3 className="font-bold text-[#183D30]">Notification preferences</h3>
          <p className="mt-2 text-sm text-[#748078]">Choose whether to show demo notifications in this interface.</p>
          <label className="mt-5 flex cursor-pointer items-center gap-3 text-sm text-[#34463B]">
            <input type="checkbox" checked={notifications} onChange={(event) => setNotifications(event.target.checked)} className="h-4 w-4 accent-[#247A58]" />
            Show notifications
          </label>
          <p className="mt-3 text-xs text-[#879188]">
            {notifications ? 'Notifications are enabled in this demo.' : 'Notifications are hidden in this demo preference.'}
          </p>
        </div>
      </>
    )
  }

  function Settings() {
    return (
      <>
        <SectionTitle title="Settings" description="Configure the sample solar installation." />
        <section className="max-w-2xl rounded-2xl border border-[#E3EAE0] bg-white p-6 sm:p-8">
          <h3 className="text-lg font-bold text-[#183D30]">Installation Details</h3>
          <div className="mt-6 space-y-5">
            <div>
              <label htmlFor="systemName" className="mb-2 block text-sm font-semibold text-[#34463B]">System name</label>
              <input id="systemName" value={systemName} onChange={(event) => setSystemName(event.target.value)} className="w-full rounded-xl border border-[#DCE5DA] px-4 py-3 text-sm outline-none focus:border-[#39845A] focus:ring-4 focus:ring-[#39845A]/10" />
            </div>
            <div>
              <label htmlFor="capacity" className="mb-2 block text-sm font-semibold text-[#34463B]">System capacity (kW)</label>
              <input id="capacity" type="number" min="0.1" step="0.1" value={capacity} onChange={(event) => setCapacity(event.target.value)} className="w-full rounded-xl border border-[#DCE5DA] px-4 py-3 text-sm outline-none focus:border-[#39845A] focus:ring-4 focus:ring-[#39845A]/10" />
            </div>
            <p className="rounded-xl bg-[#EFF6EA] p-4 text-sm leading-6 text-[#247A58]">
              Changes are held in this page's temporary state. They are not saved to a database.
            </p>
          </div>
        </section>
      </>
    )
  }

  function renderPage() {
    switch (activePage) {
      case 'Energy Analytics':
        return <EnergyAnalytics />
      case 'Weather & Forecast':
        return <WeatherForecast />
      case 'Alerts':
        return <Alerts />
      case 'Settings':
        return <Settings />
      default:
        return <Overview />
    }
  }

  return (
    <div className="min-h-screen bg-[#F6F8F5] text-[#26352E] lg:flex">
      <aside className="flex w-full flex-col border-r border-[#E4EAE3] bg-white lg:fixed lg:inset-y-0 lg:w-64">
        <div className="border-b border-[#E8EEE6] px-6 py-6">
          <Brand />
        </div>
        <div className="px-5 py-6">
          <p className="mb-4 px-3 text-[10px] font-bold tracking-[0.18em] text-[#98A39A]">WORKSPACE</p>
          <nav className="flex gap-2 overflow-x-auto lg:flex-col">
            {navItems.map((item) => (
              <button
                key={item.name}
                type="button"
                onClick={() => setActivePage(item.name)}
                aria-current={activePage === item.name ? 'page' : undefined}
                className={`flex shrink-0 items-center gap-3 rounded-xl px-4 py-3 text-left text-sm font-medium transition ${
                  activePage === item.name
                    ? 'bg-[#123D32] text-white shadow-md shadow-[#123D32]/10'
                    : 'text-[#65736A] hover:bg-[#F0F5ED] hover:text-[#174B38]'
                }`}
              >
                <span className="text-lg">{item.icon}</span>
                {item.name}
              </button>
            ))}
          </nav>
        </div>
        <div className="mt-auto hidden p-5 lg:block">
          <div className="rounded-2xl bg-[#EFF6EA] p-4">
            <div className="text-xl">☀️</div>
            <p className="mt-2 text-sm font-semibold text-[#174B38]">Clean energy, smarter choices.</p>
            <p className="mt-1 text-xs leading-5 text-[#748078]">Track your solar performance in one place.</p>
          </div>
          <p className="mt-5 text-center text-[10px] text-[#98A39A]">GRIDPULSE © 2026</p>
        </div>
      </aside>

      <main className="min-w-0 flex-1 p-5 sm:p-8 lg:ml-64 lg:p-10">
        <header className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-xs font-semibold tracking-[0.15em] text-[#39845A]">SOLAR MONITORING</p>
            <h1 className="mt-2 text-2xl font-bold tracking-tight text-[#183D30] sm:text-3xl">
              {activePage === 'Overview' ? 'Energy Overview' : activePage}
            </h1>
            <p className="mt-2 text-sm text-[#748078]">
              {activePage === 'Overview'
                ? 'Here is what is happening with your solar system.'
                : `Explore your ${activePage.toLowerCase()} workspace.`}
            </p>
          </div>
          <div className="flex items-center gap-3 rounded-xl border border-[#E3EAE0] bg-white px-4 py-3">
            <span className="h-2.5 w-2.5 rounded-full bg-[#39845A]" />
            <div>
              <p className="text-xs font-semibold text-[#174B38]">Demo System</p>
              <p className="mt-0.5 text-[10px] text-[#98A39A]">Sample data only</p>
            </div>
          </div>
        </header>

        {renderPage()}

        <footer className="mt-10 border-t border-[#E4EAE3] pt-5 text-center text-xs text-[#98A39A]">
          GridPulse · Intelligent Solar Monitoring · Demo dashboard
        </footer>
      </main>
    </div>
  )
}

export default Dashboard
