import Config
data_path = Path.join("/", "root")

# TODO: If folks want reproducible builds, we will need to
# eventually fix this.
now = NaiveDateTime.utc_now()

later =
  now
  |> NaiveDateTime.truncate(:second)
  |> NaiveDateTime.add(60 * 60 * 24 * 365 * 3, :second)

config :nerves_time, earliest_time: now, latest_time: later

config :logger, backends: [RingLogger]
config :logger, RingLogger, max_size: 1024, color: [enabled: true]

config :mdns_lite,
  mdns_config: %{host: :hostname, ttl: 120},
  services: [
    %{id: :configurator, protocol: "http", transport: "tcp", port: 80}
    # %{id: :s sh, protocol: "s s h", transport: "tcp", port: 22}
  ]

config :shoehorn,
  init: [:nerves_runtime, :vintage_net],
  handler: FarmbotOS.Platform.Target.ShoehornHandler,
  app: :farmbot

config :tzdata, :autoupdate, :disabled

config :vintage_net,
  regulatory_domain: "00",
  persistence: VintageNet.Persistence.Null,
  config: [{"wlan0", %{type: VintageNet.Technology.Null}}]

%{
  FarmbotOS.Asset.Repo => [
    database: "/root/database.#{Mix.env()}.db"
  ],
  FarmbotOS.AssetWorker.FarmbotOS.Asset.PinBinding => [
    gpio_handler: FarmbotOS.Platform.Target.PinBindingWorker.CircuitsGPIOHandler
  ],
  FarmbotOS.Leds => [
    gpio_handler: FarmbotOS.Platform.Target.Leds.CircuitsHandler
  ],
  FarmbotOS.Configurator => [
    network_layer: FarmbotOS.Platform.Target.Configurator.VintageNetworkLayer
  ],
  FarmbotOS.FileSystem => [data_path: data_path],
  FarmbotOS.Init.Supervisor => [
    init_children: [FarmbotOS.Platform.Target.RTCWorker]
  ],
  FarmbotOS.Platform.Supervisor => [
    platform_children: [
      FarmbotOS.Platform.Target.Network.Supervisor,
      FarmbotOS.Platform.Target.InfoWorker.Supervisor
    ]
  ],
  FarmbotOS.System => [system_tasks: FarmbotOS.Platform.Target.SystemTasks]
}
|> Enum.map(fn {m, c} -> config :farmbot, m, c end)
