defmodule FarmbotOS.Platform.Host.Configurator do
  @moduledoc """
  Supervisor responsible for setting up epmd and ensuring
  local environment variables are setup correctly
  """

  use Supervisor

  @doc false
  def start_link(args) do
    Supervisor.start_link(__MODULE__, args, name: __MODULE__)
  end

  defp start_node() do
    case Node.start(:"farmbot-host@127.0.0.1") do
      {:ok, _} -> :ok
      _ -> :ok
    end
  end

  def init(_) do
    start_node()
    System.get_env("FARMBOT_EMAIL") || raise error("email")
    System.get_env("FARMBOT_PASSWORD") || raise error("password")
    System.get_env("FARMBOT_SERVER") || raise error("server")
    :ignore
  end

  defp error(_field) do
    """
    Your environment is not properly configured!
    Please export FARMBOT_EMAIL, FARMBOT_PASSWORD and FARMBOT_SERVER
    in your environment.
    """
  end
end
