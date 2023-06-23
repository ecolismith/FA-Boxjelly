import React from "react";
import { connect } from "react-redux";
import {
  DesignerPanel, DesignerPanelContent,
} from "../farm_designer/designer_panel";
import { DesignerNavTabs, Panel } from "../farm_designer/panel_header";
import { envGet } from "./remote_env/selectors";
import { Photos } from "./images/photos";
import { CameraCalibration } from "./camera_calibration";
import { WeedDetector } from "./weed_detector";
import { WDENVKey } from "./remote_env/interfaces";
import { t } from "../i18next_wrapper";
import { Collapse } from "@blueprintjs/core";
import { ExpandableHeader, ToolTip } from "../ui";
import { Actions, ToolTips } from "../constants";
import { requestFarmwareUpdate } from "../farmware/farmware_info";
import { isBotOnline } from "../devices/must_be_online";
import { CaptureSettings } from "./capture_settings";
import {
  PhotoFilterSettings, FiltersEnabledWarning,
} from "./photo_filter_settings";
import { ImageShowFlags } from "./images/interfaces";
import { DesignerPhotosProps, PhotosPanelState } from "./interfaces";
import { mapStateToProps } from "./state_to_props";
import { ImagingDataManagement } from "./data_management";
import { getImageShownStatusFlags } from "./photo_filter_settings/util";
import { FarmwareName } from "../sequences/step_tiles/tile_execute_script";
import { FarmwareForm } from "../farmware/farmware_forms";
import { BooleanSetting } from "../session_keys";
import { maybeOpenPanel } from "../settings/maybe_highlight";
import { DevSettings } from "../settings/dev/dev_support";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import { Bar } from "react-chartjs-2";


export class RawDesignerPhotos
  extends React.Component<DesignerPhotosProps> {

  componentDidMount = () => this.props.dispatch(maybeOpenPanel("photos"));

  toggle = (key: keyof PhotosPanelState) => () =>
    this.props.dispatch({ type: Actions.TOGGLE_PHOTOS_PANEL_OPTION, payload: key });

  
  
  get imageShowFlags(): ImageShowFlags {
    return getImageShownStatusFlags({
      getConfigValue: this.props.getConfigValue,
      env: this.props.env,
      image: this.props.currentImage,
      designer: this.props.designer,
      size: this.props.currentImageSize,
    });
  }

  render() {
    const wDEnvGet = (key: WDENVKey) => envGet(key, this.props.wDEnv);
    const { syncStatus, botToMqttStatus, photosPanelState } = this.props;
    const botOnline = isBotOnline(syncStatus, botToMqttStatus);
    const common = {
      syncStatus,
      botToMqttStatus,
      timeSettings: this.props.timeSettings,
      dispatch: this.props.dispatch,
      images: this.props.images,
      env: this.props.env,
      currentImage: this.props.currentImage,
    };
    const elementStyle = {
      width: '430px',
      height: '288px',
    };
    
    const imageCommon = {
      flags: this.imageShowFlags,
      designer: this.props.designer,
      getConfigValue: this.props.getConfigValue,
    };
    const farmwareNames = Object.keys(this.props.farmwares);
    return <DesignerPanel panelName={"camera"} panel={Panel.Camera}>
      <DesignerNavTabs />
      <DesignerPanelContent panelName={"camera"}>
        <label>{t("Camera")}</label>
        <button>Click</button>
        
        <Photos {...common} {...imageCommon}
          currentBotLocation={this.props.currentBotLocation}
          movementState={this.props.movementState}
          arduinoBusy={this.props.arduinoBusy}
          currentImageSize={this.props.currentImageSize}
          imageJobs={this.props.imageJobs} />
          
        <ExpandableHeader
          expanded={photosPanelState.camera}
          title={t("Thermal camera images")}
          onClick={this.toggle("camera")} />
        <Collapse isOpen={photosPanelState.camera}>
        <div style={elementStyle}>
          <img src="/img_1.jpg" alt="Images cannot be found!" style={{ width: '100%', height: '100%' }} />
        </div>
        </Collapse>

      </DesignerPanelContent>
    </DesignerPanel>;
  }
}

export const DesignerPhotos = connect(mapStateToProps)(RawDesignerPhotos);

export interface UpdateImagingPackageProps {
  farmwareName: string;
  version: string | undefined;
  botOnline: boolean;
}
export const UpdateImagingPackage = (props: UpdateImagingPackageProps) =>
  props.version
    ? <div className={"update"}>
      <p>v{props.version}</p>
      <i className={"fa fa-refresh"}
        onClick={requestFarmwareUpdate(props.farmwareName, props.botOnline)} />
    </div>
    : <div className={"update"} />;
