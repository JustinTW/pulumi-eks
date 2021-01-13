# coding=utf-8
# *** WARNING: this file was generated by pulumi-gen-eks. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from .vpc_cni import VpcCni
from . import outputs
import pulumi_aws
import pulumi_kubernetes

__all__ = [
    'ClusterNodeGroupOptions',
    'CoreData',
    'NodeGroupData',
    'Taint',
]

@pulumi.output_type
class ClusterNodeGroupOptions(dict):
    """
    Describes the configuration options accepted by a cluster to create its own node groups.
    """
    def __init__(__self__, *,
                 ami_id: Optional[str] = None,
                 auto_scaling_group_tags: Optional[Mapping[str, str]] = None,
                 bootstrap_extra_args: Optional[str] = None,
                 cloud_formation_tags: Optional[Mapping[str, str]] = None,
                 cluster_ingress_rule: Optional['pulumi_aws.ec2.SecurityGroupRule'] = None,
                 desired_capacity: Optional[int] = None,
                 encrypt_root_block_device: Optional[bool] = None,
                 extra_node_security_groups: Optional[Sequence['pulumi_aws.ec2.SecurityGroup']] = None,
                 gpu: Optional[bool] = None,
                 instance_profile: Optional['pulumi_aws.iam.InstanceProfile'] = None,
                 instance_type: Optional[str] = None,
                 key_name: Optional[str] = None,
                 kubelet_extra_args: Optional[str] = None,
                 labels: Optional[Mapping[str, str]] = None,
                 max_size: Optional[int] = None,
                 min_size: Optional[int] = None,
                 node_associate_public_ip_address: Optional[bool] = None,
                 node_public_key: Optional[str] = None,
                 node_root_volume_size: Optional[int] = None,
                 node_security_group: Optional['pulumi_aws.ec2.SecurityGroup'] = None,
                 node_subnet_ids: Optional[Sequence[str]] = None,
                 node_user_data: Optional[str] = None,
                 node_user_data_override: Optional[str] = None,
                 spot_price: Optional[str] = None,
                 taints: Optional[Mapping[str, 'outputs.Taint']] = None,
                 version: Optional[str] = None):
        """
        Describes the configuration options accepted by a cluster to create its own node groups.
        :param str ami_id: The AMI ID to use for the worker nodes.
               
               Defaults to the latest recommended EKS Optimized Linux AMI from the AWS Systems Manager Parameter Store.
               
               Note: `amiId` and `gpu` are mutually exclusive.
               
               See for more details:
               - https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html.
        :param Mapping[str, str] auto_scaling_group_tags: The tags to apply to the NodeGroup's AutoScalingGroup in the CloudFormation Stack.
               
               Per AWS, all stack-level tags, including automatically created tags, and the `cloudFormationTags` option are propagated to resources that AWS CloudFormation supports, including the AutoScalingGroup. See https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html
               
               Note: Given the inheritance of auto-generated CF tags and `cloudFormationTags`, you should either supply the tag in `autoScalingGroupTags` or `cloudFormationTags`, but not both.
        :param str bootstrap_extra_args: Additional args to pass directly to `/etc/eks/bootstrap.sh`. Fror details on available options, see: https://github.com/awslabs/amazon-eks-ami/blob/master/files/bootstrap.sh. Note that the `--apiserver-endpoint`, `--b64-cluster-ca` and `--kubelet-extra-args` flags are included automatically based on other configuration parameters.
        :param Mapping[str, str] cloud_formation_tags: The tags to apply to the CloudFormation Stack of the Worker NodeGroup.
               
               Note: Given the inheritance of auto-generated CF tags and `cloudFormationTags`, you should either supply the tag in `autoScalingGroupTags` or `cloudFormationTags`, but not both.
        :param 'pulumi_aws.ec2.SecurityGroupRule' cluster_ingress_rule: The ingress rule that gives node group access.
        :param int desired_capacity: The number of worker nodes that should be running in the cluster. Defaults to 2.
        :param bool encrypt_root_block_device: Encrypt the root block device of the nodes in the node group.
        :param Sequence['pulumi_aws.ec2.SecurityGroup'] extra_node_security_groups: Extra security groups to attach on all nodes in this worker node group.
               
               This additional set of security groups captures any user application rules that will be needed for the nodes.
        :param bool gpu: Use the latest recommended EKS Optimized Linux AMI with GPU support for the worker nodes from the AWS Systems Manager Parameter Store.
               
               Defaults to false.
               
               Note: `gpu` and `amiId` are mutually exclusive.
               
               See for more details:
               - https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html
               - https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id.html
        :param 'pulumi_aws.iam.InstanceProfile' instance_profile: The ingress rule that gives node group access.
        :param str instance_type: The instance type to use for the cluster's nodes. Defaults to "t2.medium".
        :param str key_name: Name of the key pair to use for SSH access to worker nodes.
        :param str kubelet_extra_args: Extra args to pass to the Kubelet. Corresponds to the options passed in the `--kubeletExtraArgs` flag to `/etc/eks/bootstrap.sh`. For example, '--port=10251 --address=0.0.0.0'. Note that the `labels` and `taints` properties will be applied to this list (using `--node-labels` and `--register-with-taints` respectively) after to the expicit `kubeletExtraArgs`.
        :param Mapping[str, str] labels: Custom k8s node labels to be attached to each woker node. Adds the given key/value pairs to the `--node-labels` kubelet argument.
        :param int max_size: The maximum number of worker nodes running in the cluster. Defaults to 2.
        :param int min_size: The minimum number of worker nodes running in the cluster. Defaults to 1.
        :param bool node_associate_public_ip_address: Whether or not to auto-assign public IP addresses on the EKS worker nodes. If this toggle is set to true, the EKS workers will be auto-assigned public IPs. If false, they will not be auto-assigned public IPs.
        :param str node_public_key: Public key material for SSH access to worker nodes. See allowed formats at:
               https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
               If not provided, no SSH access is enabled on VMs.
        :param int node_root_volume_size: The size in GiB of a cluster node's root volume. Defaults to 20.
        :param 'pulumi_aws.ec2.SecurityGroup' node_security_group: The security group for the worker node group to communicate with the cluster.
               
               This security group requires specific inbound and outbound rules.
               
               See for more details:
               https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html
               
               Note: The `nodeSecurityGroup` option and the cluster option`nodeSecurityGroupTags` are mutually exclusive.
        :param Sequence[str] node_subnet_ids: The set of subnets to override and use for the worker node group.
               
               Setting this option overrides which subnets to use for the worker node group, regardless if the cluster's `subnetIds` is set, or if `publicSubnetIds` and/or `privateSubnetIds` were set.
        :param str node_user_data: Extra code to run on node startup. This code will run after the AWS EKS bootstrapping code and before the node signals its readiness to the managing CloudFormation stack. This code must be a typical user data script: critically it must begin with an interpreter directive (i.e. a `#!`).
        :param str node_user_data_override: User specified code to run on node startup. This code is expected to handle the full AWS EKS bootstrapping code and signal node readiness to the managing CloudFormation stack. This code must be a complete and executable user data script in bash (Linux) or powershell (Windows).
               
               See for more details: https://docs.aws.amazon.com/eks/latest/userguide/worker.html
        :param str spot_price: Bidding price for spot instance. If set, only spot instances will be added as worker node.
        :param Mapping[str, 'TaintArgs'] taints: Custom k8s node taints to be attached to each worker node. Adds the given taints to the `--register-with-taints` kubelet argument
        :param str version: Desired Kubernetes master / control plane version. If you do not specify a value, the latest available version is used.
        """
        if ami_id is not None:
            pulumi.set(__self__, "ami_id", ami_id)
        if auto_scaling_group_tags is not None:
            pulumi.set(__self__, "auto_scaling_group_tags", auto_scaling_group_tags)
        if bootstrap_extra_args is not None:
            pulumi.set(__self__, "bootstrap_extra_args", bootstrap_extra_args)
        if cloud_formation_tags is not None:
            pulumi.set(__self__, "cloud_formation_tags", cloud_formation_tags)
        if cluster_ingress_rule is not None:
            pulumi.set(__self__, "cluster_ingress_rule", cluster_ingress_rule)
        if desired_capacity is not None:
            pulumi.set(__self__, "desired_capacity", desired_capacity)
        if encrypt_root_block_device is not None:
            pulumi.set(__self__, "encrypt_root_block_device", encrypt_root_block_device)
        if extra_node_security_groups is not None:
            pulumi.set(__self__, "extra_node_security_groups", extra_node_security_groups)
        if gpu is not None:
            pulumi.set(__self__, "gpu", gpu)
        if instance_profile is not None:
            pulumi.set(__self__, "instance_profile", instance_profile)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if kubelet_extra_args is not None:
            pulumi.set(__self__, "kubelet_extra_args", kubelet_extra_args)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if min_size is not None:
            pulumi.set(__self__, "min_size", min_size)
        if node_associate_public_ip_address is not None:
            pulumi.set(__self__, "node_associate_public_ip_address", node_associate_public_ip_address)
        if node_public_key is not None:
            pulumi.set(__self__, "node_public_key", node_public_key)
        if node_root_volume_size is not None:
            pulumi.set(__self__, "node_root_volume_size", node_root_volume_size)
        if node_security_group is not None:
            pulumi.set(__self__, "node_security_group", node_security_group)
        if node_subnet_ids is not None:
            pulumi.set(__self__, "node_subnet_ids", node_subnet_ids)
        if node_user_data is not None:
            pulumi.set(__self__, "node_user_data", node_user_data)
        if node_user_data_override is not None:
            pulumi.set(__self__, "node_user_data_override", node_user_data_override)
        if spot_price is not None:
            pulumi.set(__self__, "spot_price", spot_price)
        if taints is not None:
            pulumi.set(__self__, "taints", taints)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="amiId")
    def ami_id(self) -> Optional[str]:
        """
        The AMI ID to use for the worker nodes.

        Defaults to the latest recommended EKS Optimized Linux AMI from the AWS Systems Manager Parameter Store.

        Note: `amiId` and `gpu` are mutually exclusive.

        See for more details:
        - https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html.
        """
        return pulumi.get(self, "ami_id")

    @property
    @pulumi.getter(name="autoScalingGroupTags")
    def auto_scaling_group_tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags to apply to the NodeGroup's AutoScalingGroup in the CloudFormation Stack.

        Per AWS, all stack-level tags, including automatically created tags, and the `cloudFormationTags` option are propagated to resources that AWS CloudFormation supports, including the AutoScalingGroup. See https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html

        Note: Given the inheritance of auto-generated CF tags and `cloudFormationTags`, you should either supply the tag in `autoScalingGroupTags` or `cloudFormationTags`, but not both.
        """
        return pulumi.get(self, "auto_scaling_group_tags")

    @property
    @pulumi.getter(name="bootstrapExtraArgs")
    def bootstrap_extra_args(self) -> Optional[str]:
        """
        Additional args to pass directly to `/etc/eks/bootstrap.sh`. Fror details on available options, see: https://github.com/awslabs/amazon-eks-ami/blob/master/files/bootstrap.sh. Note that the `--apiserver-endpoint`, `--b64-cluster-ca` and `--kubelet-extra-args` flags are included automatically based on other configuration parameters.
        """
        return pulumi.get(self, "bootstrap_extra_args")

    @property
    @pulumi.getter(name="cloudFormationTags")
    def cloud_formation_tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags to apply to the CloudFormation Stack of the Worker NodeGroup.

        Note: Given the inheritance of auto-generated CF tags and `cloudFormationTags`, you should either supply the tag in `autoScalingGroupTags` or `cloudFormationTags`, but not both.
        """
        return pulumi.get(self, "cloud_formation_tags")

    @property
    @pulumi.getter(name="clusterIngressRule")
    def cluster_ingress_rule(self) -> Optional['pulumi_aws.ec2.SecurityGroupRule']:
        """
        The ingress rule that gives node group access.
        """
        return pulumi.get(self, "cluster_ingress_rule")

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[int]:
        """
        The number of worker nodes that should be running in the cluster. Defaults to 2.
        """
        return pulumi.get(self, "desired_capacity")

    @property
    @pulumi.getter(name="encryptRootBlockDevice")
    def encrypt_root_block_device(self) -> Optional[bool]:
        """
        Encrypt the root block device of the nodes in the node group.
        """
        return pulumi.get(self, "encrypt_root_block_device")

    @property
    @pulumi.getter(name="extraNodeSecurityGroups")
    def extra_node_security_groups(self) -> Optional[Sequence['pulumi_aws.ec2.SecurityGroup']]:
        """
        Extra security groups to attach on all nodes in this worker node group.

        This additional set of security groups captures any user application rules that will be needed for the nodes.
        """
        return pulumi.get(self, "extra_node_security_groups")

    @property
    @pulumi.getter
    def gpu(self) -> Optional[bool]:
        """
        Use the latest recommended EKS Optimized Linux AMI with GPU support for the worker nodes from the AWS Systems Manager Parameter Store.

        Defaults to false.

        Note: `gpu` and `amiId` are mutually exclusive.

        See for more details:
        - https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-ami.html
        - https://docs.aws.amazon.com/eks/latest/userguide/retrieve-ami-id.html
        """
        return pulumi.get(self, "gpu")

    @property
    @pulumi.getter(name="instanceProfile")
    def instance_profile(self) -> Optional['pulumi_aws.iam.InstanceProfile']:
        """
        The ingress rule that gives node group access.
        """
        return pulumi.get(self, "instance_profile")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[str]:
        """
        The instance type to use for the cluster's nodes. Defaults to "t2.medium".
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[str]:
        """
        Name of the key pair to use for SSH access to worker nodes.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="kubeletExtraArgs")
    def kubelet_extra_args(self) -> Optional[str]:
        """
        Extra args to pass to the Kubelet. Corresponds to the options passed in the `--kubeletExtraArgs` flag to `/etc/eks/bootstrap.sh`. For example, '--port=10251 --address=0.0.0.0'. Note that the `labels` and `taints` properties will be applied to this list (using `--node-labels` and `--register-with-taints` respectively) after to the expicit `kubeletExtraArgs`.
        """
        return pulumi.get(self, "kubelet_extra_args")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, str]]:
        """
        Custom k8s node labels to be attached to each woker node. Adds the given key/value pairs to the `--node-labels` kubelet argument.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[int]:
        """
        The maximum number of worker nodes running in the cluster. Defaults to 2.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[int]:
        """
        The minimum number of worker nodes running in the cluster. Defaults to 1.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter(name="nodeAssociatePublicIpAddress")
    def node_associate_public_ip_address(self) -> Optional[bool]:
        """
        Whether or not to auto-assign public IP addresses on the EKS worker nodes. If this toggle is set to true, the EKS workers will be auto-assigned public IPs. If false, they will not be auto-assigned public IPs.
        """
        return pulumi.get(self, "node_associate_public_ip_address")

    @property
    @pulumi.getter(name="nodePublicKey")
    def node_public_key(self) -> Optional[str]:
        """
        Public key material for SSH access to worker nodes. See allowed formats at:
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
        If not provided, no SSH access is enabled on VMs.
        """
        return pulumi.get(self, "node_public_key")

    @property
    @pulumi.getter(name="nodeRootVolumeSize")
    def node_root_volume_size(self) -> Optional[int]:
        """
        The size in GiB of a cluster node's root volume. Defaults to 20.
        """
        return pulumi.get(self, "node_root_volume_size")

    @property
    @pulumi.getter(name="nodeSecurityGroup")
    def node_security_group(self) -> Optional['pulumi_aws.ec2.SecurityGroup']:
        """
        The security group for the worker node group to communicate with the cluster.

        This security group requires specific inbound and outbound rules.

        See for more details:
        https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html

        Note: The `nodeSecurityGroup` option and the cluster option`nodeSecurityGroupTags` are mutually exclusive.
        """
        return pulumi.get(self, "node_security_group")

    @property
    @pulumi.getter(name="nodeSubnetIds")
    def node_subnet_ids(self) -> Optional[Sequence[str]]:
        """
        The set of subnets to override and use for the worker node group.

        Setting this option overrides which subnets to use for the worker node group, regardless if the cluster's `subnetIds` is set, or if `publicSubnetIds` and/or `privateSubnetIds` were set.
        """
        return pulumi.get(self, "node_subnet_ids")

    @property
    @pulumi.getter(name="nodeUserData")
    def node_user_data(self) -> Optional[str]:
        """
        Extra code to run on node startup. This code will run after the AWS EKS bootstrapping code and before the node signals its readiness to the managing CloudFormation stack. This code must be a typical user data script: critically it must begin with an interpreter directive (i.e. a `#!`).
        """
        return pulumi.get(self, "node_user_data")

    @property
    @pulumi.getter(name="nodeUserDataOverride")
    def node_user_data_override(self) -> Optional[str]:
        """
        User specified code to run on node startup. This code is expected to handle the full AWS EKS bootstrapping code and signal node readiness to the managing CloudFormation stack. This code must be a complete and executable user data script in bash (Linux) or powershell (Windows).

        See for more details: https://docs.aws.amazon.com/eks/latest/userguide/worker.html
        """
        return pulumi.get(self, "node_user_data_override")

    @property
    @pulumi.getter(name="spotPrice")
    def spot_price(self) -> Optional[str]:
        """
        Bidding price for spot instance. If set, only spot instances will be added as worker node.
        """
        return pulumi.get(self, "spot_price")

    @property
    @pulumi.getter
    def taints(self) -> Optional[Mapping[str, 'outputs.Taint']]:
        """
        Custom k8s node taints to be attached to each worker node. Adds the given taints to the `--register-with-taints` kubelet argument
        """
        return pulumi.get(self, "taints")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Desired Kubernetes master / control plane version. If you do not specify a value, the latest available version is used.
        """
        return pulumi.get(self, "version")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class CoreData(dict):
    """
    Defines the core set of data associated with an EKS cluster, including the network in which it runs.
    """
    def __init__(__self__, *,
                 cluster: 'pulumi_aws.eks.Cluster',
                 cluster_security_group: 'pulumi_aws.ec2.SecurityGroup',
                 endpoint: str,
                 instance_roles: Sequence['pulumi_aws.iam.Role'],
                 node_group_options: 'outputs.ClusterNodeGroupOptions',
                 provider: 'pulumi_kubernetes.Provider',
                 subnet_ids: Sequence[str],
                 vpc_id: str,
                 aws_provider: Optional['pulumi_aws.Provider'] = None,
                 eks_node_access: Optional['pulumi_kubernetes.core.v1.ConfigMap'] = None,
                 fargate_profile: Optional['pulumi_aws.eks.FargateProfile'] = None,
                 kubeconfig: Optional[Any] = None,
                 node_security_group_tags: Optional[Mapping[str, str]] = None,
                 oidc_provider: Optional['pulumi_aws.iam.OpenIdConnectProvider'] = None,
                 private_subnet_ids: Optional[Sequence[str]] = None,
                 public_subnet_ids: Optional[Sequence[str]] = None,
                 storage_classes: Optional[Mapping[str, 'pulumi_kubernetes.storage.v1.StorageClass']] = None,
                 tags: Optional[Mapping[str, str]] = None,
                 vpc_cni: Optional['VpcCni'] = None):
        """
        Defines the core set of data associated with an EKS cluster, including the network in which it runs.
        """
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "cluster_security_group", cluster_security_group)
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "instance_roles", instance_roles)
        pulumi.set(__self__, "node_group_options", node_group_options)
        pulumi.set(__self__, "provider", provider)
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)
        if aws_provider is not None:
            pulumi.set(__self__, "aws_provider", aws_provider)
        if eks_node_access is not None:
            pulumi.set(__self__, "eks_node_access", eks_node_access)
        if fargate_profile is not None:
            pulumi.set(__self__, "fargate_profile", fargate_profile)
        if kubeconfig is not None:
            pulumi.set(__self__, "kubeconfig", kubeconfig)
        if node_security_group_tags is not None:
            pulumi.set(__self__, "node_security_group_tags", node_security_group_tags)
        if oidc_provider is not None:
            pulumi.set(__self__, "oidc_provider", oidc_provider)
        if private_subnet_ids is not None:
            pulumi.set(__self__, "private_subnet_ids", private_subnet_ids)
        if public_subnet_ids is not None:
            pulumi.set(__self__, "public_subnet_ids", public_subnet_ids)
        if storage_classes is not None:
            pulumi.set(__self__, "storage_classes", storage_classes)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vpc_cni is not None:
            pulumi.set(__self__, "vpc_cni", vpc_cni)

    @property
    @pulumi.getter
    def cluster(self) -> 'pulumi_aws.eks.Cluster':
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter(name="clusterSecurityGroup")
    def cluster_security_group(self) -> 'pulumi_aws.ec2.SecurityGroup':
        return pulumi.get(self, "cluster_security_group")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="instanceRoles")
    def instance_roles(self) -> Sequence['pulumi_aws.iam.Role']:
        return pulumi.get(self, "instance_roles")

    @property
    @pulumi.getter(name="nodeGroupOptions")
    def node_group_options(self) -> 'outputs.ClusterNodeGroupOptions':
        return pulumi.get(self, "node_group_options")

    @property
    @pulumi.getter
    def provider(self) -> 'pulumi_kubernetes.Provider':
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[str]:
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="awsProvider")
    def aws_provider(self) -> Optional['pulumi_aws.Provider']:
        return pulumi.get(self, "aws_provider")

    @property
    @pulumi.getter(name="eksNodeAccess")
    def eks_node_access(self) -> Optional['pulumi_kubernetes.core.v1.ConfigMap']:
        return pulumi.get(self, "eks_node_access")

    @property
    @pulumi.getter(name="fargateProfile")
    def fargate_profile(self) -> Optional['pulumi_aws.eks.FargateProfile']:
        return pulumi.get(self, "fargate_profile")

    @property
    @pulumi.getter
    def kubeconfig(self) -> Optional[Any]:
        return pulumi.get(self, "kubeconfig")

    @property
    @pulumi.getter(name="nodeSecurityGroupTags")
    def node_security_group_tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "node_security_group_tags")

    @property
    @pulumi.getter(name="oidcProvider")
    def oidc_provider(self) -> Optional['pulumi_aws.iam.OpenIdConnectProvider']:
        return pulumi.get(self, "oidc_provider")

    @property
    @pulumi.getter(name="privateSubnetIds")
    def private_subnet_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "private_subnet_ids")

    @property
    @pulumi.getter(name="publicSubnetIds")
    def public_subnet_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "public_subnet_ids")

    @property
    @pulumi.getter(name="storageClasses")
    def storage_classes(self) -> Optional[Mapping[str, 'pulumi_kubernetes.storage.v1.StorageClass']]:
        return pulumi.get(self, "storage_classes")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vpcCni")
    def vpc_cni(self) -> Optional['VpcCni']:
        return pulumi.get(self, "vpc_cni")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class NodeGroupData(dict):
    """
    NodeGroupData describes the resources created for the given NodeGroup.
    """
    def __init__(__self__, *,
                 auto_scaling_group_name: str,
                 cfn_stack: 'pulumi_aws.cloudformation.Stack',
                 extra_node_security_groups: Sequence['pulumi_aws.ec2.SecurityGroup'],
                 node_security_group: 'pulumi_aws.ec2.SecurityGroup'):
        """
        NodeGroupData describes the resources created for the given NodeGroup.
        :param str auto_scaling_group_name: The AutoScalingGroup name for the node group.
        :param 'pulumi_aws.cloudformation.Stack' cfn_stack: The CloudFormation Stack which defines the Node AutoScalingGroup.
        :param Sequence['pulumi_aws.ec2.SecurityGroup'] extra_node_security_groups: The additional security groups for the node group that captures user-specific rules.
        :param 'pulumi_aws.ec2.SecurityGroup' node_security_group: The security group for the node group to communicate with the cluster.
        """
        pulumi.set(__self__, "auto_scaling_group_name", auto_scaling_group_name)
        pulumi.set(__self__, "cfn_stack", cfn_stack)
        pulumi.set(__self__, "extra_node_security_groups", extra_node_security_groups)
        pulumi.set(__self__, "node_security_group", node_security_group)

    @property
    @pulumi.getter(name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """
        The AutoScalingGroup name for the node group.
        """
        return pulumi.get(self, "auto_scaling_group_name")

    @property
    @pulumi.getter(name="cfnStack")
    def cfn_stack(self) -> 'pulumi_aws.cloudformation.Stack':
        """
        The CloudFormation Stack which defines the Node AutoScalingGroup.
        """
        return pulumi.get(self, "cfn_stack")

    @property
    @pulumi.getter(name="extraNodeSecurityGroups")
    def extra_node_security_groups(self) -> Sequence['pulumi_aws.ec2.SecurityGroup']:
        """
        The additional security groups for the node group that captures user-specific rules.
        """
        return pulumi.get(self, "extra_node_security_groups")

    @property
    @pulumi.getter(name="nodeSecurityGroup")
    def node_security_group(self) -> 'pulumi_aws.ec2.SecurityGroup':
        """
        The security group for the node group to communicate with the cluster.
        """
        return pulumi.get(self, "node_security_group")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class Taint(dict):
    """
    Represents a Kubernetes `taint` to apply to all Nodes in a NodeGroup. See https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/.
    """
    def __init__(__self__, *,
                 effect: str,
                 value: str):
        """
        Represents a Kubernetes `taint` to apply to all Nodes in a NodeGroup. See https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/.
        :param str effect: The effect of the taint.
        :param str value: The value of the taint.
        """
        pulumi.set(__self__, "effect", effect)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def effect(self) -> str:
        """
        The effect of the taint.
        """
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the taint.
        """
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

